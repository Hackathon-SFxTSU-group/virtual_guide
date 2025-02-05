import { Routes } from '@angular/router';

export const routes: Routes = [
  {
    path: '',
    loadComponent: () => import('./image-uploader/image-uploader.component').then((m) => m.ImageUploader),
  },
];
