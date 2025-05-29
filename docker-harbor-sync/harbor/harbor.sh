#!/usr/bin/env bash

set -euo pipefail

: '
Harbor initialisation consists of
* creating a public project to host Tanzu platform images
* importing kapp-controller
* importing Tanzu packages
'

usage() {
    cat <<EOF
Usage: $0 -h HARBOR_HOST -p HARBOR_PASSWORD [ -u HARBOR_USERNAME ]
EOF
}

KAPP_CONTROLLER_URL=projects.registry.vmware.com/tkg/kapp-controller:v0.25.0_vmware.1
TANZU_PROJECT=tkg
TANZU_PACKAGES_URL=projects.registry.vmware.com/tkg/packages/standard/repo:v1.4.0
HARBOR_USERNAME=admin

while getopts 'h:p:u:' opt; do
    case "$opt" in
        h)
            HARBOR_HOST="$OPTARG"
            ;;
        p)
            HARBOR_PASSWORD="$OPTARG"
            ;;
        u)
            HARBOR_USERNAME="$OPTARG"
            ;;
        *)
            echo "ERROR: invalid option" >&2
            usage
            exit 1
    esac
done

shift $((OPTIND-1))

[ -z "${HARBOR_HOST}" ]  && echo "ERROR: Mandatory HARBOR_HOST argument missing" >&2 && usage >&2 && exit 1
[ -z "${HARBOR_PASSWORD}" ]  && echo "ERROR: Mandatory HARBOR_PASSWORD argument missing" >&2 && usage >&2 && exit 1
[ -z "${HARBOR_USERNAME}" ]  && echo "ERROR: HARBOR_USERNAME argument cannot be blank" >&2 && usage >&2 && exit 1

HARBOR_BASIC_AUTH_B64=$(echo -n "${HARBOR_USERNAME}:${HARBOR_PASSWORD}" | base64)

# create Harbor project via API
curl -sSfk -X PUT \
  -H 'Accept: application/json' \
  -H 'X-Resource-Name-In-Location: false' \
  -H 'Content-Type: application/json' \
  -H "Authorization: Basic ${HARBOR_BASIC_AUTH_B64}" \
  -d "{
  \"metadata\": {
    \"public\": \"true\"
  }
}"  https://${HARBOR_HOST}/api/v2.0/projects/${TANZU_PROJECT} || \
curl -fk -X 'POST' \
  -H 'Accept: application/json' \
  -H 'X-Resource-Name-In-Location: false' \
  -H 'Content-Type: application/json' \
  -H "Authorization: Basic ${HARBOR_BASIC_AUTH_B64}" \
  -d "{
  \"project_name\": \"${TANZU_PROJECT}\",
  \"public\": true,
  \"storage_limit\": 0
}"  https://${HARBOR_HOST}/api/v2.0/projects


curl -sSfLo /usr/local/bin/imgpkg https://github.com/vmware-tanzu/carvel-imgpkg/releases/download/v0.29.0/imgpkg-linux-amd64 && chmod +x /usr/local/bin/imgpkg

TMPKAPP=$(mktemp)
TMPPKGS=$(mktemp)

set -x

imgpkg copy -i ${KAPP_CONTROLLER_URL} --to-tar ${TMPKAPP}
HTTP_PROXY= HTTPS_PROXY= NO_PROXY= http_proxy= https_proxy= no_proxy= imgpkg copy --tar ${TMPKAPP} --to-repo ${HARBOR_HOST}/${TANZU_PROJECT}/kapp-controller --registry-verify-certs=false --registry-username=${HARBOR_USERNAME} --registry-password=${HARBOR_PASSWORD}

# # use the imgpkg copy command to download the packages and to pack them into a tarball
imgpkg copy -b ${TANZU_PACKAGES_URL} --to-tar ${TMPPKGS}
# # use the imgpkg copy command to `push` the content into your private container registry
HTTP_PROXY= HTTPS_PROXY= NO_PROXY= http_proxy= https_proxy= no_proxy= imgpkg copy --tar ${TMPPKGS} --to-repo ${HARBOR_HOST}/${TANZU_PROJECT}/packages --registry-verify-certs=false --registry-username=${HARBOR_USERNAME} --registry-password=${HARBOR_PASSWORD}

rm $TMPKAPP $TMPPKGS
