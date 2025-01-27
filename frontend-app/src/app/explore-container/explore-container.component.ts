import {Component, Input} from '@angular/core';
import {IonButton} from "@ionic/angular/standalone";
import { Camera, CameraResultType, CameraSource, Photo } from '@capacitor/camera';

@Component({
  selector: 'app-explore-container',
  templateUrl: './explore-container.component.html',
  styleUrls: ['./explore-container.component.scss'],
  imports: [IonButton]
})
export class ExploreContainerComponent {
  @Input() name?: string;

  imagePath?: string;
  file?: File;

  async openGallery() {
    const image = await Camera.getPhoto({
      source: CameraSource.Photos,
      resultType: CameraResultType.Uri,
    });

    if (image.webPath) {
      this.file = await this.downloadImage(image);
      this.imagePath = image.webPath;
    }
  }

  async downloadImage(image: Photo) {
    const response = await fetch(image.webPath!);
    const blob = await response.blob();
    const filename = image.webPath!.split('/').pop() ?? `photo.${image.format}`;
    return new File([blob], filename, { type: blob.type });
  }
}
