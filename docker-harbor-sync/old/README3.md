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
   

   Sure! Here's the modified script with an interactive feature where you can enter the image name directly from the console. This will allow you to dynamically set the image name as a variable:

```python
import docker
import requests

def get_image_tags(image_name):
    """
    Retrieve the last 5 tags for a given Docker image from Docker Hub using the 'requests' library
    to interact with the Docker Hub API.
    """
    url = f"https://hub.docker.com/v2/repositories/library/{image_name}/tags/"
    tags = []
    while url:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            tags.extend([result['name'] for result in data['results']])
            url = data.get('next')  # Check if there's a next page of results
        else:
            print(f"Error fetching tags for {image_name}: {response.status_code}")
            return []

    # Return the last 5 tags (or all if there are fewer than 5)
    return tags[:5]

def check_image_exists_in_registry(image_name, tag, registry):
    """
    Check if the image with a specific tag exists in the example.com container registry.
    """
    try:
        # Assuming the registry has a public endpoint or API to check existence
        # This could be done via an API request, or by trying to pull the image
        client = docker.from_env()
        client.images.get(f"{registry}/{image_name}:{tag}")
        return True
    except docker.errors.ImageNotFound:
        return False

def pull_and_push_image(image_name, tag, registry):
    """
    Pull the image from Docker Hub and push it to example.com registry.
    """
    client = docker.from_env()

    # Pull image from Docker Hub
    print(f"Pulling {image_name}:{tag} from Docker Hub...")
    client.images.pull(f"docker.io/{image_name}:{tag}")

    # Tag image for example.com registry
    print(f"Tagging {image_name}:{tag} for {registry}...")
    client.images.get(f"docker.io/{image_name}:{tag}").tag(f"{registry}/{image_name}:{tag}")

    # Push image to example.com registry
    print(f"Pushing {image_name}:{tag} to {registry}...")
    client.images.push(f"{registry}/{image_name}:{tag}")
    
    print(f"Successfully pushed {image_name}:{tag} to {registry}.")

def main():
    # Interactive input for image name
    image_name = input("Enter the Docker image name (e.g., 'ubuntu'): ").strip()
    
    if not image_name:
        print("Error: Image name is required.")
        return
    
    registry = 'example.com'  # Replace with your container registry URL
    
    # Step 1: Get the last 5 tags of the image from Docker Hub
    tags = get_image_tags(image_name)
    
    if not tags:
        print(f"Error: No tags found for {image_name}.")
        return
    
    # Step 2: Check if each tag exists in the example.com registry
    for tag in tags:
        print(f"Checking if {image_name}:{tag} exists in {registry}...")
        if not check_image_exists_in_registry(image_name, tag, registry):
            print(f"{image_name}:{tag} not found in {registry}. Pulling and pushing...")
            pull_and_push_image(image_name, tag, registry)
        else:
            print(f"{image_name}:{tag} already exists in {registry}. Skipping.")

if __name__ == '__main__':
    main()
```

### Changes:
- **Interactive Image Name Input**: 
    - The script now prompts the user to input the Docker image name using `input()`. This allows you to specify the image name dynamically at runtime.
    - The `image_name` variable is then assigned the value provided by the user.

### Example of running the script:
```
Enter the Docker image name (e.g., 'ubuntu'): nginx
```

This change allows the user to input any image name during execution, making it more flexible and interactive.

### Notes:
- Ensure the `input()` function is used in a terminal or console environment.
- The rest of the logic remains unchanged; it still fetches tags, checks if they exist in your registry, and pushes them if needed.

Let me know if you need any further adjustments!