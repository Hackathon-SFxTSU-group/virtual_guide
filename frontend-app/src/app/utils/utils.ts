import {API_URL} from "../consts/consts";

// TODO
const api = 'http://45.151.62.93:8000';

export function getUploadedImagePath(imageUrl: string) {
  return `${api}${imageUrl}`;
}
