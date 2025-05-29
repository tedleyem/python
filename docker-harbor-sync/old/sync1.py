#!/bin/python
import docker
import subprocess

def get_image_tags(image_name):
    """
    Retrieve the last 5 tags for a given Docker image from Docker Hub using the 'docker hub'
    API. Replace this with an actual request to Docker Hub's API or a Docker registry API.
    """
    # Replace this with logic to fetch tags from DockerHub.
    # You can use requests to hit Docker Hub's API to get tags.
    return ['latest', 'v1.0', 'v0.9', 'v0.8', 'v0.7']  # Sample tags

def check_image_exists_in_registry(image_name, tag, registry):
    """
    Check if the image with a specific tag exists in the example.com container registry.
    For simplicity, this is mocked up as we don't have direct access to example.com API.
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
