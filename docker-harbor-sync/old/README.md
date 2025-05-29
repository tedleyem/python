# Docker image sync
#  Python script that uses the Docker API to do the following: 
# 1. Pull an image from Docker Hub
# 2. Check if the last 5 versions of the image exist in a given registry (example.com)
# 3. If not found at example.com, then pull those versions from Docker Hub and push them to the example.com registry.

## Requirements 
```bash
pip install docker
```

### How it works:
1. **Get Image Tags**: The function `get_image_tags` provides a list of tags for the image (this is mocked in the script, you should replace it with actual logic to fetch tags from Docker Hub).
   
2. **Check Image Existence**: The `check_image_exists_in_registry` function tries to check whether a specific version of the image exists in the given registry (`example.com`). It uses the Docker client to attempt fetching the image.

3. **Pull and Push**: If an image version is not found in the registry, `pull_and_push_image` pulls the image from Docker Hub, tags it with the correct registry URL, and then pushes it to the registry.

4. **Main Function**: The `main` function is responsible for iterating over the last 5 image tags and checking if they exist in the registry. If they don’t exist, it pulls from Docker Hub and pushes them to `example.com`.

### Assumptions:
- The Docker Hub API is not directly queried for tags in this script, but you can replace the mock implementation with a real call using something like the `requests` library to interact with Docker Hub’s API and get the tags.
  
- Example.com is a placeholder for your actual container registry (it could be any private registry you use).

Make sure to handle any potential errors properly (e.g., network errors, authentication issues, etc.) based on your environment and specific requirements.