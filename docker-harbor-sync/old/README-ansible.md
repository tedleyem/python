# Docker image sync
#  Python script that uses the Docker API to do the following: 
# 1. Pull an image from Docker Hub
# 2. Check if the last 5 versions of the image exist in a given registry (example.com)
# 3. If not found at example.com, then pull those versions from Docker Hub and push them to the example.com registry.

    Prompting for Image Name:
        The vars_prompt is used to ask for the Docker image name interactively when the playbook runs.

    Retrieving Docker Hub Tags:
        The uri module sends a GET request to the Docker Hub API to retrieve the tags for the specified image.
        The response is parsed and the first 5 tags are extracted using the set_fact module.

    Checking if Tags Exist in the Example Registry:
        The docker_image module checks if the image (with the given tags) already exists in the example registry (example.com).
        The ignore_errors: yes ensures the playbook continues even if the image is not found.

    Pulling and Pushing Missing Images:
        If an image does not exist in the example registry, the playbook will pull it from Docker Hub and push it to example.com.
        The docker_image module's source parameter is used for the pull and push actions.
        If the tag is not found in the registry (i.e., failed in check_results), it will trigger the block to pull, tag, and push the image.