import os
from itertools import zip_longest

import numpy as np


# Helper method to group several segments into one which represents one input (with class 0 or 1)
def segmentsGrouper(n_inputs, iterable, fillvalue=np.float64(0)):
    """grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx."""
    args = [iter(iterable)] * n_inputs
    fv = [fillvalue] * len(iterable[0])
    return zip_longest(fillvalue=list(fv), *args)


# Helper method to label the segments interictal = 0, preictal = 1
def labeler(example, index):
    # return example, tf.cast(index, tf.int64)
    return np.append(example, np.int64(index))


def loadData(
    data_directory, file_names, group_segments_form_input, n_segments_form_input
):
    # Load interictal and preictal segments from npy files
    labeled_data_sets = []
    for i, file_name in enumerate(file_names):
        loaded_segments = np.load(os.path.join(data_directory, file_name))

        # If group_segments_form_input, group several segments into one, to form one input
        if group_segments_form_input:
            loaded_segments = list(
                segmentsGrouper(n_segments_form_input, loaded_segments)
            )  # grouped segments

        print("-----> loaded_segments shape", np.shape(loaded_segments))

        # Annotate the segments
        labeled_dataset = list(map(lambda ex: labeler(ex, i), loaded_segments))
        print("-----> labeled_dataset shape", np.shape(labeled_dataset))

        labeled_data_sets.append(labeled_dataset)

    print("Interictal segments: ", np.shape(labeled_data_sets[0]))
    print("Preictal segments: ", np.shape(labeled_data_sets[1]))

    # Merge the two segments' lists (interictal and preictal) into one
    all_labeled_data = np.concatenate(labeled_data_sets)
    print("All data: ", np.shape(all_labeled_data))

    # Get the data and the labels
    X, Y = all_labeled_data[:, :-1], all_labeled_data[:, -1]
    Y = Y.astype(int)  # cast the labels to int64

    return X, Y
