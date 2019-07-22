import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { WizardComponent } from './wizard/wizard.component';
const routes: Routes = [    
  { path: '', pathMatch: 'full', component: HomeComponent }, 
  { path: 'getRecipe', component: WizardComponent}
]

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
