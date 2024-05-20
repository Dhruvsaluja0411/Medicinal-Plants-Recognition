import h5py

# Load the HDF5 file
with h5py.File('plant_classification_model_DenseNet201.h5', 'r') as f:
    # Create a new HDF5 file in write mode
    with h5py.File('plant_classification_model_DenseNet201_modified.h5', 'w') as f_modified:
        # Iterate through groups in the original HDF5 file
        for group_name in f.keys():
            # Create corresponding groups in the new HDF5 file
            group = f_modified.create_group(group_name)
            # Iterate through datasets in the group
            for dataset_name in f[group_name].keys():
                # Copy datasets from the original file to the new file
                f[group_name].copy(dataset_name, group)
