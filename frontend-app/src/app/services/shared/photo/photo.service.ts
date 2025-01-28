import {Camera, CameraResultType, CameraSource, Photo} from "@capacitor/camera";

export abstract class PhotoService {
  async getPhoto() {
    const image = await Camera.getPhoto({
      source: CameraSource.Photos,
      resultType: CameraResultType.Uri,
    });

    const file = await this.getFile(image);

    return {
      src: image.webPath!,
      file: file,
    }
  }

  async getFile(image: Photo) {
    const response = await fetch(image.webPath!);
    const blob = await response.blob();
    const filename = this.getFileName(image);
    return new File([blob], filename, { type: blob.type });
  }

  abstract getFileName(image: Photo): string;
}
