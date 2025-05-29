# Docker image sync
#  Python script that uses the Docker API to do the following: 
# 1. Pull an image from Docker Hub
# 2. Check if the last 5 versions of the image exist in a given registry (example.com)
# 3. If not found at example.com, then pull those versions from Docker Hub and push them to the example.com registry.

## Requirements 
```bash
pip install requests
```

1. **Fetching Tags with `requests`**:
    - The `get_image_tags` function now uses the `requests` library to send a `GET` request to the Docker Hub API endpoint for fetching tags for a given image.
    - The endpoint URL is `https://hub.docker.com/v2/repositories/library/{image_name}/tags/`, where `{image_name}` is the name of your Docker image.
    - The API returns a paginated list of tags, so the function loops through the pages (`next` field in the response) until it has all available tags.
    - The function then returns the first 5 tags (or fewer if there are less than 5).

2. **Handling Errors**:
    - If the request to Docker Hub fails (non-200 status code), the function will print an error message and return an empty list of tags.

3. **Main Function**:
    - The main function now prints an error message and stops if no tags are found for the specified image.

### How it works:
- Make sure your Docker environment is set up correctly and that you have permission to push to the target registry (`example.com` in this case).
- The Docker Hub API limits the number of tags returned per request (usually 10), so the code is designed to handle pagination by using the `next` field in the response.
   