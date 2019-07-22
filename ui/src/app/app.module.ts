//System Imports
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations';
import { MaterialModule } from './material/material.module';
import { HttpClientModule } from '@angular/common/http';
import 'hammerjs';
import { HomeComponent } from './home/home.component';
import { CameraComponent } from './camera/camera.component';
import { WizardComponent } from './wizard/wizard.component';
import { FancyCardComponent } from './fancy-card/fancy-card.component';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    CameraComponent,
    WizardComponent,
    FancyCardComponent,
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    AppRoutingModule,
    HttpClientModule,
    MaterialModule,
    FormsModule,
    ReactiveFormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
