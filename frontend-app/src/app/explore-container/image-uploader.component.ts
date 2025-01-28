import {ChangeDetectionStrategy, Component, inject, signal} from '@angular/core';
import {IonButton} from "@ionic/angular/standalone";
import {Optional} from "../types/optional.type";
import {PhotoService} from "../services/shared/photo/photo.service";
import {ApiService} from "../services/shared/api/api.service";

@Component({
  selector: 'app-image-uploader',
  templateUrl: './image-uploader.component.html',
  styleUrls: ['./image-uploader.component.scss'],
  imports: [IonButton],
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class ImageUploader {
  imagePath = signal<Optional<string>>(null);
  file = signal<Optional<File>>(null);

  private readonly photoService = inject(PhotoService);

  private readonly apiService = inject(ApiService);

  async getPhoto() {
    const photoData = await this.photoService.getPhoto();

    this.imagePath.set(photoData.src);
    this.file.set(photoData.file);

    // this.uploadFile();
  }

  uploadFile() {
    return this.apiService.uploadImage(this.file()!).subscribe();
  }
}
