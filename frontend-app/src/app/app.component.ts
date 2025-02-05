import {ChangeDetectionStrategy, Component, inject} from '@angular/core';
import {IonApp, IonRouterOutlet, IonSpinner} from '@ionic/angular/standalone';
import {LoaderService} from "./services/shared/loader/loader.service";

@Component({
  selector: 'app-root',
  templateUrl: 'app.component.html',
  styleUrls: ['app.component.scss'],
  imports: [IonApp, IonRouterOutlet, IonSpinner],
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class AppComponent {
  loaderService = inject(LoaderService);
}
