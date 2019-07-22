import {map} from 'rxjs/operators';
import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { BehaviorSubject } from 'rxjs';
const httpOptions = {//Headers to fix Cross-Origin issues
  headers: new HttpHeaders({ 'Content-Type': 'application/json' })
};

@Injectable({
  providedIn: 'root'
})
export class RecipeService {
  
  recipe_results: BehaviorSubject<any> = new BehaviorSubject<any>([]);

  constructor(private http: HttpClient) { }

  getRecipes(content){
      return this.http.post('http://localhost:5000/foodie/api/watson', content, { headers: httpOptions.headers, responseType: 'json'}).pipe(
        map(res => {
          return res;
        }));
  }

  makeRecipe(content){ 
    return this.http.post('http://localhost:5000/foodie/api/recipes', content, { headers: httpOptions.headers, responseType: 'json'}).pipe(
      map(res => {
        this.recipe_results.next(res);
        return res;
      }));
  }

  getFinalRecipe(){ 
    return this.recipe_results.asObservable();
  }
}
