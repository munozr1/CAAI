# CAAI
# Verifying Image Contents using OpenSSL and Public Key

In this guide, we'll walk through the process of verifying the contents of an image file using the command line, OpenSSL, and your public key.

## Prerequisites

Before we begin, ensure you have the following:

- The image file you want to verify (`image.jpg`)
- Your public key (`public.pem`)
- OpenSSL installed on your system

## Steps

1. **Convert Image to Binary**

   Start by converting the image file to binary. You can achieve this using the `xxd` command:

   ```bash
   xxd -p image.jpg > image.bin

2. **Verify the Image**

   Next, verify the image using OpenSSL and your public key:

   ```bash
   openssl dgst -sha256 -verify public.pem -signature image.bin.sha256 image.bin
   ```

   This command will verify the image contents using your public key.
