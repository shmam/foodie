import { Component, OnInit, Input } from '@angular/core';
import { calcPossibleSecurityContexts } from '@angular/compiler/src/template_parser/binding_parser';
// import { link } from 'fs';

@Component({
  selector: 'fancy-card',
  templateUrl: './fancy-card.component.html',
  styleUrls: ['./fancy-card.component.scss']
})
export class FancyCardComponent implements OnInit {
  @Input() labelName: String;
  @Input() imgSrc;
  @Input() link;
  @Input() calories;
  @Input() ingredients;
  public stringOfIngredients = "";
  constructor() { }

  ngOnInit() {
    this.calories = Math.round(this.calories);
    for (var i = 0; i < this.ingredients.length; i++){
      this.stringOfIngredients += this.ingredients[i] + ", ";
    }
    
  }

}
