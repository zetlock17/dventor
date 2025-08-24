export function fileToBlob(file: File): Blob {
  return new Blob([file], { type: file.type });
}

export function blobToFile(blob: Blob, fileName: string): File {
  return new File([blob], fileName, { type: blob.type });
}