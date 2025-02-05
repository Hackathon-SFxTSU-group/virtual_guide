import {Injectable, signal} from "@angular/core";

@Injectable({
  providedIn: 'root'
})
export class LoaderService {
  private readonly loading = signal<boolean>(false);

  isLoading = this.loading.asReadonly();

  enable() {
    this.loading.set(true);
  }

  disable() {
    this.loading.set(false);
  }
}
