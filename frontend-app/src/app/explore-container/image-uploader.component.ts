import {ChangeDetectionStrategy, Component, inject, signal} from '@angular/core';
import {IonButton, IonInput, IonItem} from "@ionic/angular/standalone";
import {Optional} from "../types/optional.type";
import {PhotoService} from "../services/shared/photo/photo.service";
import {ApiService} from "../services/shared/api/api.service";
import {IPredictResponse, IProcessedPhotoData, IQuestionResponse, IUploadResponse} from "../interfaces/interfaces";
import {finalize, switchMap, tap} from "rxjs";
import {getUploadedImagePath} from "../utils/utils";
import {InputChangeEventDetail} from "@ionic/angular";
import {LoaderService} from "../services/shared/loader/loader.service";

@Component({
  selector: 'app-image-uploader',
  templateUrl: './image-uploader.component.html',
  styleUrls: ['./image-uploader.component.scss'],
  imports: [IonButton, IonInput, IonItem],
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class ImageUploader {
  imagePreview = signal<Optional<string>>(null);
  file = signal<Optional<File>>(null);
  predictedInfo = signal<Optional<string>>(null);
  question = signal<string>('');
  answer = signal<string>('');

  private readonly photoService = inject(PhotoService);

  private readonly apiService = inject(ApiService);

  private readonly loaderService = inject(LoaderService);

  async getPhoto() {
    const photoData = await this.photoService.getPhoto();

    this.setPhotoData(photoData);
  }

  async takePhoto() {
    const photoData = await this.photoService.takePhoto();

    this.setPhotoData(photoData);
  }

  recognizeImage() {
    this.loaderService.enable();

    this.apiService.uploadImage(this.file()!)
      .pipe(
        tap((uploadData: IUploadResponse) => {
          this.imagePreview.set(getUploadedImagePath(uploadData.image_url));
        }),
        switchMap((uploadData: IUploadResponse) => {
          return this.apiService.predict({ image_url: uploadData.image_url });
        }),
        tap((predictData: IPredictResponse) => {
          this.predictedInfo.set(predictData.predicted_class);
        }),
        finalize(() => {
          this.loaderService.disable();
        }),
      )
      .subscribe();
  }

  onChange(event: CustomEvent<InputChangeEventDetail>) {
    this.question.set(event.detail.value ?? '');
  }

  askQuestion() {
    this.loaderService.enable();

    this.apiService.ask({ question: this.question() })
      .pipe(
        tap((questionResponse: IQuestionResponse) => {
          this.answer.set(questionResponse.answer)
        }),
        finalize(() => {
          this.loaderService.disable();
        }),
      )
      .subscribe()
  }

  private setPhotoData(photoData: IProcessedPhotoData) {
    this.clearData();

    this.imagePreview.set(photoData.src);
    this.file.set(photoData.file);
  }

  private clearData() {
    this.predictedInfo.set(null);
    this.question.set('');
    this.answer.set('');
  }
}
