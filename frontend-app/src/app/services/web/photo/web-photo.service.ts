import {Injectable} from '@angular/core';
import {Photo} from "@capacitor/camera";
import {PhotoService} from "../../shared/photo/photo.service";

@Injectable()
export class WebPhotoService extends PhotoService {
  override getFileName(image: Photo): string {
    const name = image.webPath!.split('/').pop() ?? 'photo';
    return `${name}.${image.format}`
  }
}
