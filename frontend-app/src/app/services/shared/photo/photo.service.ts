import {Camera, CameraResultType, CameraSource, Photo} from "@capacitor/camera";
import {IProcessedPhotoData} from "../../../interfaces/interfaces";
import {Directive, inject} from "@angular/core";
import {LoaderService} from "../loader/loader.service";

@Directive()
export abstract class PhotoService {
  private readonly loaderService = inject(LoaderService);

  async getPhoto() {
    return this.processGetPhoto(CameraSource.Photos)
  }

  async takePhoto() {
    return this.processGetPhoto(CameraSource.Camera)
  }

  private async processGetPhoto(cameraSource: CameraSource): Promise<IProcessedPhotoData> {
    const image = await Camera.getPhoto({
      source: cameraSource,
      resultType: CameraResultType.Uri,
    });

    const file = await this.getFile(image);

    return {
      src: image.webPath!,
      file: file,
    }
  }

  async getFile(image: Photo) {
    this.loaderService.enable();

    const response = await fetch(image.webPath!);
    const blob = await response.blob();
    const filename = this.getFileName(image);

    this.loaderService.disable();

    return new File([blob], filename, { type: blob.type });
  }

  abstract getFileName(image: Photo): string;
}
