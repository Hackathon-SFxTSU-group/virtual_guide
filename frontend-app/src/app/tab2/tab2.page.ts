import {ChangeDetectionStrategy, Component} from '@angular/core';
import { IonHeader, IonToolbar, IonTitle, IonContent } from '@ionic/angular/standalone';
import { ImageUploader } from '../explore-container/image-uploader.component';

@Component({
  selector: 'app-tab2',
  templateUrl: 'tab2.page.html',
  styleUrls: ['tab2.page.scss'],
  imports: [IonHeader, IonToolbar, IonTitle, IonContent, ImageUploader],
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class Tab2Page {
}
