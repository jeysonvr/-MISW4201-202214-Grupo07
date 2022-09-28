import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
    providedIn: 'root'
})
export class UsuarioService {

    private backUrl: string = "http://127.0.0.1:5000"

    constructor(private http: HttpClient) { }

    userLogIn(usuario: string, contrasena: string): Observable<any>{
        console.log('Iniando servicio login');
        return this.http.post<any>(`${this.backUrl}/login`, { "usuario": usuario, "contrasena": contrasena });
    }    
}
