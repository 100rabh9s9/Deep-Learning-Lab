import kagglehub

# Download dataset
path = kagglehub.dataset_download(
    "hasibalmuzdadid/shoe-vs-sandal-vs-boot-dataset-15k-images"
)

print("Dataset downloaded to:", path)