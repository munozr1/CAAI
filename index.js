// const { ExifTool } = require('exiftool-vendored');
const exiftool = require("exiftool-vendored").exiftool


const imagePath = process.argv[2];

async function printImageMetadata(imagePath) {

    try {
        const metadata = await exiftool.readMetadata(imagePath, ['-File:all']);
        console.log("Image Metadata:", metadata.data[0]);
    } catch (error) {
        console.error("Error reading image metadata:", error);
    } finally {
        exiftool.end();
    }
}

printImageMetadata(imagePath);
