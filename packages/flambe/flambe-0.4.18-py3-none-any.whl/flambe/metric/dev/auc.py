import torch
import sklearn.metrics
import numpy as np

from flambe.metric.metric import Metric


def one_hot(indices: torch.Tensor, width: int) -> torch.Tensor:
    """Converts a list of ints into 1-hot format.

    Parameters
    ----------
    indices: torch.Tensor
        the indices to be converted
    width: int
        the width of the 1-hot encoding (= the maximal index value)

    Returns
    -------
    torch.Tensor
        A one-hot representation of the input indices.
    """
    indices = indices.squeeze()
    return torch.zeros(indices.size(0), width).scatter_(1, indices.unsqueeze(1), 1.)


class AUC(Metric):

    def __init__(self, max_fpr=1.0):
        """Initialize the AUC metric.

        Parameters
        ----------
        max_fpr : float, optional
            Maximum false positive rate to compute the area under
        """
        self.max_fpr = max_fpr

    def __str__(self) -> str:
        """Return the name of the Metric (for use in logging)."""
        return f'{self.__class__.__name__}@{self.max_fpr}'

    def compute(self, pred: torch.Tensor, target: torch.Tensor) -> torch.Tensor:
        """Compute AUC at the given max false positive rate.

        Parameters
        ----------
        pred : torch.Tensor
            The model predictions of shape numsamples
        target : torch.Tensor
            The binary targets of shape numsamples

        Returns
        -------
        torch.Tensor
            The computed AUC

        """
        scores = np.array(pred)
        targets = np.array(target)

        # Case when number of elements added are 0
        if not scores.size or not targets.size:
            return torch.tensor(0.5)

        fpr, tpr, _ = sklearn.metrics.roc_curve(targets, scores, sample_weight=None)

        # Compute the area under the curve using trapezoidal rule
        max_index = np.searchsorted(fpr, [self.max_fpr], side='right').item()

        # Ensure we integrate up to max_fpr
        fpr, tpr = fpr.tolist(), tpr.tolist()
        fpr, tpr = fpr[:max_index], tpr[:max_index]
        fpr.append(self.max_fpr)
        tpr.append(max(tpr))

        area = np.trapz(tpr, fpr)

        return torch.tensor(area / self.max_fpr).float()


class MultiClassAUC(AUC):
    """N-Ary (Multiclass) AUC for k-way classification"""

    def compute(self, pred: torch.Tensor, target: torch.Tensor) -> torch.Tensor:
        """Compute multiclass AUC at the given max false positive rate.

        Parameters
        ----------
        pred : torch.Tensor
            The model predictions of shape numsamples x numclasses
        target : torch.Tensor
            The binary targets of shape:
             - numsamples. In this case the elements index into the
               different classes
             - numsamples x numclasses. This implementation only
               considers the indices of the max values as positive
               labels

        Returns
        -------
        torch.Tensor
            The computed AUC
        """
        if pred.numel() == target.numel() == 0:
            return 0.5 * pred.new_ones(size=(1, 1)).squeeze()
        num_samples, num_classes = pred.shape
        pred_reshaped = pred.reshape(-1)
        if target.numel() == num_samples:
            # target consists of indices
            target = one_hot(target, num_classes)
        else:
            # reconstructing targets to make sure that only
            # one target is provided by taking the argmax along an axis
            target = torch.argmax(target, dim=1)
            target = one_hot(target, num_classes)
        target_reshaped = target.reshape(-1)
        if pred_reshaped.size() != target_reshaped.size():
            raise RuntimeError(
                'Predictions could not be flattened for AUC computation. '
                'Ensure all batches are the same size '
                '(hint: try setting `drop_last = True` in Sampler).')

        return super().compute(pred_reshaped, target_reshaped)
