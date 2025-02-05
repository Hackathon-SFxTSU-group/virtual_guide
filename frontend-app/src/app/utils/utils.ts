import {API_URL} from "../consts/consts";

export function getUploadedImagePath(imageUrl: string) {
  return `${API_URL}${imageUrl}`;
}
