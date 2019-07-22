import { Component, OnInit } from '@angular/core';
import { RecipeService } from '../services/recipe.service';
@Component({
  selector: 'app-wizard',
  templateUrl: './wizard.component.html',
  styleUrls: ['./wizard.component.scss']
})
export class WizardComponent implements OnInit {

  public res;
  public hits = [];

  constructor(private recipeService: RecipeService) { }

  ngOnInit() {
  }

  changeThis(){
    this.recipeService.getFinalRecipe().subscribe(res => {
        console.log(res);
        this.res = res;
        this.hits = this.res.hits;
        console.log(this.hits);
        document.getElementById("spinner").style.display = "none";
    },
    err => {
        console.error("An error has occured while retrieving data content! " + err);
    }
    );
  }

}
