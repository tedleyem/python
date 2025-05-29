#!/usr/bin/env bash

set -euo pipefail

HARBOR_OPTIONS="--with-notary --with-trivy"
HARBOR_VERSION=v2.5.2

HARBOR_SIGN_KEY_HEX=644FF454C0B4115C

cd $(realpath $(dirname $0))

HARBOR_OFFLINE_TARBALL=https://github.com/goharbor/harbor/releases/download/${HARBOR_VERSION}/harbor-offline-installer-${HARBOR_VERSION}.tgz
HARBOR_OFFLINE_ASC=${HARBOR_OFFLINE_TARBALL}.asc

curl -fsSL --connect-timeout 10 -o harbor-offline-installer.tgz ${HARBOR_OFFLINE_TARBALL}
curl -fsSL --connect-timeout 10 -o harbor-offline-installer.tgz.asc ${HARBOR_OFFLINE_ASC}

curl -fsSL "https://keyserver.ubuntu.com/pks/lookup?op=get&options=mr&search=0x${HARBOR_SIGN_KEY_HEX}" | gpg --import
gpg -v --keyserver hkps://keyserver.ubuntu.com --verify harbor-offline-installer.tgz.asc

tar xzf harbor-offline-installer.tgz
cd harbor
[ -e ../harbor.yml ] && ln -s ../harbor.yml

./install.sh ${HARBOR_OPTIONS}
