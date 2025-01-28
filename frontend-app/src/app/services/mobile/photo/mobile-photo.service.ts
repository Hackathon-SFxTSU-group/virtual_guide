import { Injectable } from '@angular/core';
import {Photo} from "@capacitor/camera";
import {PhotoService} from "../../shared/photo/photo.service";

@Injectable()
export class MobilePhotoService extends PhotoService {
  override getFileName(image: Photo): string {
    return image.webPath!.split('/').pop() ?? `photo.${image.format}`;
  }
}
