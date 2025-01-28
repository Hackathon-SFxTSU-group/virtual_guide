import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ImageUploader } from './image-uploader.component';

describe('ExploreContainerComponent', () => {
  let component: ImageUploader;
  let fixture: ComponentFixture<ImageUploader>;

  beforeEach(async () => {
    fixture = TestBed.createComponent(ImageUploader);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
