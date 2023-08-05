import logging
import multiprocessing as mp

import torch
from torch.utils.data import DataLoader, Dataset, ConcatDataset, Subset
from torchvision import transforms

import gammalearn.utils as utils


def create_datasets_memory(datafiles_list, experiment):
    """
    Create datasets from datafiles list, data are loaded in memory.
    Parameters
    ----------
    datafiles (List) : files to load data from
    experiment (Experiment): the experiment

    Returns
    -------
    Dataset
    """
    logger = logging.getLogger(__name__ + '.create_datasets_memory')

    logger.info('Start creating datasets')

    assert datafiles_list, 'The data file list is empty !'

    if experiment.data_transform is not None:
        transform = transforms.Compose(experiment.data_transform['data'])
        target_transform = transforms.Compose(experiment.data_transform['target'])
        telescope_transform = transforms.Compose(experiment.data_transform['telescope'])
    else:
        transform = None
        target_transform = None
        telescope_transform = None

    def create_dataset():
        torch.set_num_threads(1)
        while True:
            if input_queue.empty():
                break
            else:
                file = input_queue.get()
                if utils.is_datafile_healthy(file):
                    dataset = experiment.dataset_class(file,
                                                       targets=experiment.targets,
                                                       transform=transform,
                                                       target_transform=target_transform,
                                                       telescope_transform=telescope_transform,
                                                       **experiment.dataset_parameters
                                                       )
                    if experiment.image_filter is not None:
                        dataset.filter_image(experiment.image_filter)
                    if experiment.event_filter is not None:
                        dataset.filter_event(experiment.event_filter)
                    if len(dataset) > 0:
                        datasets.append(dataset)
                    else:
                        logger.debug('Dataset from file {} is empty after filtering. Ignored'.format(file))
                else:
                    logger.debug('Datafile {} contains empty dataset(s). Ignored'.format(file))

    with mp.Manager() as manager:
        input_queue = mp.Queue()
        logger.info('length of data file list : {}'.format(len(datafiles_list)))
        for f in datafiles_list:
            input_queue.put(f)
        datasets = manager.list()
        if experiment.preprocessing_workers > 0:
            num_workers = experiment.preprocessing_workers
        else:
            num_workers = 1
        workers = [mp.Process(target=create_dataset) for _ in range(num_workers)]
        for w in workers:
            w.start()
        input_queue.close()
        for w in workers:
            w.join()

        datasets = list(datasets)
        logger.info('Data set created')
        input_queue.join_thread()

    return datasets


def create_dataloaders(datasets, experiment):
    """
    Create dataloaders from the training dataset according to the validating ratio
    Parameters
    ----------
    datasets (list or Dataset): list of datasets or Dataset
    experiment (Experiment): the experiment

    Returns
    -------
    Training and validating data loaders
    """
    logger = logging.getLogger(__name__ + '.create_dataloaders')
    batch_size = experiment.batch_size
    validating_ratio = experiment.validating_ratio
    num_workers = experiment.dataloader_workers
    pin_memory = experiment.pin_memory

    assert datasets, 'Dataset is empty !'

    # Creation of subset train and test
    if experiment.split_by_file:
        train_max_index = int(len(datasets) * (1 - validating_ratio))
        logger.debug('Index max of training set : {}'.format(train_max_index))

        shuffled_indices = torch.randperm(len(datasets)).numpy()
        train_datasets = [datasets[i] for i in shuffled_indices[:train_max_index]]
        val_datasets = [datasets[i] for i in shuffled_indices[train_max_index:]]

        if experiment.data_augment is not None:
            logger.info('Start data augmentation')
            train_datasets = experiment.data_augment['function'](train_datasets, **experiment.data_augment['kwargs'])

        train_set = ConcatDataset(train_datasets)
    else:
        datasets = ConcatDataset(datasets)
        train_max_index = int(len(datasets) * (1 - validating_ratio))
        logger.debug('Index max of training set : {}'.format(train_max_index))

        shuffled_indices = torch.randperm(len(datasets)).numpy()
        assert isinstance(datasets, Dataset)
        train_datasets = Subset(datasets, shuffled_indices[:train_max_index])
        val_datasets = [Subset(datasets, shuffled_indices[train_max_index:])]

        if experiment.data_augment is not None:
            logger.info('Start data augmentation')
            train_datasets = experiment.data_augment['function']([train_datasets], **experiment.data_augment['kwargs'])
            train_set = ConcatDataset(train_datasets)
        else:
            train_set = train_datasets

    training_loader = DataLoader(train_set,
                                 batch_size=batch_size,
                                 shuffle=True,
                                 drop_last=True,
                                 num_workers=num_workers,
                                 pin_memory=pin_memory)
    logger.info('training set length : {}'.format(len(train_set)))
    logger.info('training loader length : {} batches'.format(len(training_loader)))

    if validating_ratio > 0:
        val_set = ConcatDataset(val_datasets)
        try:
            assert len(val_set) > 0
        except AssertionError as e:
            logger.exception('Validating set must contain data')
            raise e
        logger.info('validating set length : {}'.format(len(val_set)))
        validating_loader = DataLoader(val_set,
                                       batch_size=batch_size,
                                       shuffle=True,
                                       num_workers=num_workers,
                                       drop_last=True,
                                       pin_memory=pin_memory)
        logger.info('validating loader length : {} batches'.format(len(validating_loader)))
    else:
        validating_loader = None

    logger.info('Data loaders created')

    return training_loader, validating_loader


def create_test_dataloaders(datasets, experiment):
    """
    Create dataloaders from the training dataset according to the validating ratio
    Parameters
    ----------
    datasets (list or Dataset): list of datasets or Dataset
    experiment (Experiment): the experiment

    Returns
    -------
    Test data loader
    """
    logger = logging.getLogger(__name__ + '.create_dataloaders')
    batch_size = experiment.batch_size
    num_workers = experiment.dataloader_workers
    pin_memory = experiment.pin_memory

    dataset = ConcatDataset(datasets)

    loader = DataLoader(dataset, batch_size=batch_size, shuffle=True,
                        drop_last=True, num_workers=num_workers, pin_memory=pin_memory)
    logger.info('test set length : {}'.format(len(dataset)))
    logger.info('test loader length : {} batches'.format(len(loader)))

    return loader
