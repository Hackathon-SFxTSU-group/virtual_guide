import {inject, Injectable} from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {
  IPredictRequest,
  IPredictResponse,
  IQuestionRequest,
  IQuestionResponse,
  IUploadResponse
} from "../../../interfaces/interfaces";
import {API_URL} from "../../../consts/consts";

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private readonly http = inject(HttpClient);

  uploadImage(file: File): Observable<IUploadResponse> {
    const formData = new FormData();
    formData.append('file', file);

    return this.http.post<IUploadResponse>(`${API_URL}/upload`, formData);
  }

  predict(predictedRequest: IPredictRequest): Observable<IPredictResponse> {
    return this.http.post<IPredictResponse>(`${API_URL}/predict`, predictedRequest);
  }

  ask(questionRequest: IQuestionRequest): Observable<IQuestionResponse> {
    return this.http.post<IQuestionResponse>(`${API_URL}/ask`, questionRequest);
  }
}
