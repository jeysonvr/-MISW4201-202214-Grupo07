import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { JwtHelperService } from "@auth0/angular-jwt";
import { UsuarioService } from '../usuario.service';

@Component({
  selector: 'app-usuario-login',
  templateUrl: './usuario-login.component.html',
  styleUrls: ['./usuario-login.component.css']
})
export class UsuarioLoginComponent implements OnInit {

  helper = new JwtHelperService();

  constructor(
    private usuarioService: UsuarioService,
    private router: Router
  ) {}

  error: boolean = false

  ngOnInit() {
  }

  onLogInUsuario(usuario: string, contrasena: string) {
    this.error = false
    this.usuarioService.userLogIn(usuario, contrasena)
      .subscribe(res => {
        const decodedToken = this.helper.decodeToken(res.token);   
        alert('El usuario realizo la consulta satisfactoriamente')     
      },
        error => {
          console.log(error);
          switch (error.status) {
            case 404:
              alert('No existe el usuario')
              break;
            case 401:
              alert('El usuario no esta autorizado')
              break;
            default:
              alert('Error')
              break;
          }          
        })
  } 
}
