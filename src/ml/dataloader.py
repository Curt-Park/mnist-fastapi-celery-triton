"""Functions for data handling.

- Author: Jinwoo Park
- Email: www.jwpark.co.kr@gmail.com
"""

from typing import Any, Dict, Tuple

from torch.utils.data.dataloader import DataLoader
from torchvision import datasets, transforms


def get_preprocessor() -> transforms.Compose:
    """Get a preprocessor for mnist."""
    transform_seq = [transforms.ToTensor(), transforms.Normalize((0.1307,), (0.3081,))]
    transform = transforms.Compose(transform_seq)
    return transform


def get_dataloaders(
    batch_size: int, test_batch_size: int, use_cuda: bool
) -> Tuple[DataLoader, DataLoader]:
    """Get dataloaders for training and test."""
    # set kwargs for training and test
    cuda_kwargs = {"num_workers": 1, "pin_memory": True, "shuffle": True}
    train_kwargs: Dict[str, Any] = {"batch_size": batch_size}
    test_kwargs: Dict[str, Any] = {"batch_size": test_batch_size}
    train_kwargs.update(cuda_kwargs if use_cuda else {})
    test_kwargs.update(cuda_kwargs if use_cuda else {})

    # set dataset loaders
    transform = get_preprocessor()
    data_path = "../../data"
    dataset1 = datasets.MNIST(data_path, train=True, download=True, transform=transform)
    dataset2 = datasets.MNIST(data_path, train=False, transform=transform)
    train_loader = DataLoader(dataset1, **train_kwargs)
    test_loader = DataLoader(dataset2, **test_kwargs)

    return train_loader, test_loader
