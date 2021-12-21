import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { BASE_URL} from '../constants';
@Component({
  selector: 'app-detection',
  templateUrl: './detection.component.html',
  styleUrls: ['./detection.component.css']
})
export class DetectionComponent implements OnInit {

  showResult = false;

  selectedFile:any;

  result:any

  constructor(private http:HttpClient) { }

  ngOnInit(): void {
  }

  onFileSelected(event:any){
  	this.selectedFile = <File>event.target.files[0]

  }

  onSubmit(data:any){

  	const form = new FormData();
  	form.append('image',this.selectedFile,this.selectedFile.name);
  		this.http.post(BASE_URL+'stroke/detection',form)
  	.subscribe((result)=>{
      this.showResult = true;
      this.result = result;
  		console.warn(result);
  	})
  	console.warn(data);
  }

}
