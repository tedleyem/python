import requests

def get_docker_image_tags(image_name):
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

# Example usage:
image_name = "redis"  # Replace with your desired Docker image name
tags = get_docker_image_tags(image_name)
print(f"Last 5 tags for {image_name}: {tags}")
