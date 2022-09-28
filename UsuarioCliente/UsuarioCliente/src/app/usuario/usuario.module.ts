import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';
import { ReactiveFormsModule } from '@angular/forms';
import { Usuario } from './usuario';
import { UsuarioLoginComponent } from './usuario-login/usuario-login.component';


@NgModule({
  declarations: [UsuarioLoginComponent],
  imports: [
    CommonModule, ReactiveFormsModule
  ],
  exports: [UsuarioLoginComponent]
})
export class UsuarioModule { }
