#!/bin/python
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
    image_name = 'your_image_name'  # Replace with your image name
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
