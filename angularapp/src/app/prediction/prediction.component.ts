import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { BASE_URL} from '../constants';

@Component({
  selector: 'app-prediction',
  templateUrl: './prediction.component.html',
  styleUrls: ['./prediction.component.css']
})
export class PredictionComponent implements OnInit {

  showResult = false;

  result:any

  constructor(private http:HttpClient) { }

  ngOnInit(): void {
  }

  onSubmit(data:any){

  	this.http.post(BASE_URL+'stroke/prediction',data)
  	.subscribe((result)=>{
      this.showResult = true;
      this.result = result;
  		console.warn(result);
  	})
  	console.warn(data);

  }

}
