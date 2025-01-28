import {EnvironmentProviders, Provider} from "@angular/core";
import {Platform} from "@ionic/angular";
import {WebPhotoService} from "./web/photo/web-photo.service";
import {MobilePhotoService} from "./mobile/photo/mobile-photo.service";
import {PhotoService} from "./shared/photo/photo.service";

export const platformServices: Array<Provider | EnvironmentProviders> = [
  {
    provide: PhotoService,
    useFactory: (platform: Platform) => {
      if (platform.is('hybrid')) {
        return new MobilePhotoService();
      }

      return new WebPhotoService();
    },
    deps: [Platform]
  }
]
