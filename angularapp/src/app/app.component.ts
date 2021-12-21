import { Component } from '@angular/core';


import { MODULE } from './app.enum' ;



@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'App';
  currentModule = MODULE.Detection;


  checkModule(){
  	if(this.currentModule == MODULE.Prediction)
  		return true;
  	return false;
  }


  updateModule(module:any){
   this.currentModule = (module == 0)?MODULE.Prediction:MODULE.Detection;
  }

}
