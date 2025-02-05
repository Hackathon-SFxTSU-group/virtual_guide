export interface IUploadResponse {
  filename: string;
  format: string;
  image_url: string;
  size: IUploadFileSize;
}

export interface IUploadFileSize {
  width: number;
  height: number;
}

export interface IPredictRequest {
  image_url: string;
}

export interface IPredictResponse {
  predicted_class: string;
}

export interface IQuestionRequest {
  question: string;
}

export interface IQuestionResponse {
  answer: string;
}

export interface IProcessedPhotoData {
  src: string;
  file: File;
}
