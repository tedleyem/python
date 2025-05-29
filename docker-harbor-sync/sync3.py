import docker
import requests
from docker.errors import ImageNotFound

image_names = [
    "python",  # Replace with your list of Docker image names
    "nginx",
    "alpine",
    "ubuntu",
    "redis"
]

harbor_url = "http://dev.example.com:8000"  # Replace with your Harbor registry URL
project_name = "library"  # Replace with your Harbor project name
robot_username = "robot$robo-linux"
robot_password = "KcQzGPxpW0wjtCn"

def get_docker_image_tags(image_name):
    """
    Grab the last 5 tags for a given Docker image from Docker Hub using the 'requests' library
    to interact with the Docker Hub API.
    """
    url = f"https://hub.docker.com/v2/repositories/library/{image_name}/tags/"
    response = requests.get(url)
    
    if response.status_code == 200:
        tags_data = response.json()
        tags = [tag['name'] for tag in tags_data['results']]

        # Get the last 5 tags
        last_5_tags = tags[:5]
        return last_5_tags
    else:
        print(f"Failed to retrieve tags for {image_name}. Status code: {response.status_code}")
        return []

def check_tag_exists_in_harbor(tag, harbor_url, project_name, repository_name):
    harbor_api_url = f"{harbor_url}/api/v2.0/projects/{project_name}/repositories/{repository_name}/tags/{tag}"
    response = requests.get(harbor_api_url)
    
    if response.status_code == 200:
        return True  # Tag exists
    elif response.status_code == 404:
        return False  # Tag does not exist
    else:
        print(f"Error checking tag {tag}: {response.status_code}")
        return False
        
def pull_image_locally(image_name, tag):
    client = docker.from_env()
    image_tag = f"{image_name}:{tag}"
    
    try:
        # Try to pull the image from Docker Hub if not found locally
        print(f"Pulling image {image_tag} locally...")
        client.images.pull(image_name, tag=tag)
        print(f"Successfully pulled image {image_tag}.")
    except Exception as e:
        print(f"Failed to pull image {image_tag}: {e}")

def push_image_to_harbor(image_name, tag, harbor_url, project_name, robot_username, robot_password):
    client = docker.from_env()
    image_tag = f"{image_name}:{tag}"
    harbor_image = f"{harbor_url}/{project_name}/{image_name}:{tag}"

    try:
        # Authenticate Docker client with Harbor robot credentials
        client.login(username=robot_username, password=robot_password, registry=harbor_url)
        
        # Tag the image with the Harbor registry destination
        image = client.images.get(image_tag)
        image.tag(harbor_image)
        
        # Push the image to Harbor
        print(f"Pushing image {image_tag} to Harbor: {harbor_image}")
        client.images.push(harbor_image)
        print(f"Successfully pushed image {harbor_image}.")
    except Exception as e:
        print(f"Failed to push image {image_tag} to Harbor: {e}")

def check_tags_in_harbor_for_multiple_images(image_names, harbor_url, project_name, robot_username, robot_password):
    # Initialize Docker client
    client = docker.from_env()

    # Loop through the list of image names
    for image_name in image_names:
        print(f"\nChecking tags for image: {image_name}")
        
        # Step 1: Retrieve the last 5 tags from Docker Hub for the current image
        tags = get_docker_image_tags(image_name)
        if not tags:
            print(f"No tags retrieved for {image_name}.")
            continue

        # Step 2: Check if each of the last 5 tags exists in the Harbor registry
        for tag in tags:
            exists = check_tag_exists_in_harbor(tag, harbor_url, project_name, image_name)
            print(f"  Tag '{tag}' exists in Harbor: {exists}")
            
            # If the tag does not exist in Harbor, try pulling it locally and pushing to Harbor
            if not exists:
                try:
                    # Check if the image with the specific tag exists locally
                    client.images.get(f"{image_name}:{tag}")
                    print(f"  Tag '{tag}' found locally.")
                except ImageNotFound:
                    # Image not found locally, pull it from Docker Hub
                    pull_image_locally(image_name, tag)
                
                # After pulling, push it to Harbor using robot credentials
                push_image_to_harbor(image_name, tag, harbor_url, project_name, robot_username, robot_password)


def main():
    # Loop through image list, check if images exists, pull and push if it doesnt. 
    check_tags_in_harbor_for_multiple_images(image_names, harbor_url, project_name, robot_username, robot_password)

if __name__ == '__main__':
    main()
