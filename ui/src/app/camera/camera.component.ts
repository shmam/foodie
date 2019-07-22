import { Component, OnInit, ViewChild, ElementRef } from '@angular/core';
import { saveAs } from 'file-saver';
import { RecipeService } from '../services/recipe.service';

    @Component({
    selector: 'camera',
    templateUrl: './camera.component.html',
    styleUrls: ['./camera.component.scss']
    })
    export class CameraComponent implements OnInit {
    @ViewChild("video")
    public video: ElementRef;

    @ViewChild("canvas")
    public canvas: ElementRef;

    public captures: Array<any>;

    public arrayOfIngredients = [];
    public constructor(public recipeService: RecipeService) {
        this.captures = [];
    }

    public ngOnInit() { }

    public ngAfterViewInit() {
        if(navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
            navigator.mediaDevices.getUserMedia({ video: true }).then(stream => {
                this.video.nativeElement.srcObject = stream;
                this.video.nativeElement.play();
            });
        }
    }

    public capture() {
        var context = this.canvas.nativeElement.getContext("2d").drawImage(this.video.nativeElement, 0, 0, 640, 480);
        var generatedID = {img: `${this.makeid(7)}.png`};
        this.recipeService.getRecipes(generatedID).subscribe(res => {
                console.log(res);
                if (res[0] === 'non-food'){
                    alert("Food was not recognized. Please scan again.");
                }
                else {
                    this.captures.push({dataURL:this.canvas.nativeElement.toDataURL("image/png"),
                                        name: res[0]
                    });
                    this.arrayOfIngredients.push(res[0]);
                }},
            err => {
                console.error("An error has occured while retrieving data content! " + err);
            }
            );
        saveAs(this.canvas.nativeElement.toDataURL("image/png"), generatedID.img);
    }

    public recipe(){ 
        var json_obj = {ingredients: this.arrayOfIngredients}
        this.recipeService.makeRecipe(json_obj).subscribe(res => {
            this.recipeService.getFinalRecipe();
            console.log(res);
        }, 
        err =>{ 
            console.error("An error has occured when calling the recpie api! " + err);
        })
    }

    public makeid(length) {
        var result           = '';
        var characters       = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
        var charactersLength = characters.length;
        for ( var i = 0; i < length; i++ ) {
        result += characters.charAt(Math.floor(Math.random() * charactersLength));
        }
        return result;
    }
}
