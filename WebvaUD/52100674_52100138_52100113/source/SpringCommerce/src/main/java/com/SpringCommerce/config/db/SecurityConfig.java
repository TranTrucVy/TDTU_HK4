package com.SpringCommerce.config.db;

import java.util.List;

//import org.springframework.beans.factory.annotation.Autowired;
//import org.springframework.context.annotation.Bean;
//
//import org.springframework.context.annotation.Configuration;
//import org.springframework.security.authentication.dao.DaoAuthenticationProvider;
//import org.springframework.security.config.annotation.authentication.builders.AuthenticationManagerBuilder;
//import org.springframework.security.config.annotation.method.configuration.EnableGlobalMethodSecurity;
//import org.springframework.security.config.annotation.method.configuration.EnableMethodSecurity;
////import org.springframework.security.config.annotation.method.configuration.EnableMethodSecurity;
//import org.springframework.security.config.annotation.web.builders.HttpSecurity;
//import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
//import org.springframework.security.config.annotation.web.configuration.WebSecurityCustomizer;
//import org.springframework.security.core.userdetails.User;
//import org.springframework.security.core.userdetails.UserDetails;
//import org.springframework.security.core.userdetails.UserDetailsService;
//import org.springframework.security.provisioning.InMemoryUserDetailsManager;
//import org.springframework.security.web.SecurityFilterChain;
//import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
//import org.springframework.security.crypto.password.PasswordEncoder;
//import org.springframework.security.config.http.*;
//import org.springframework.http.HttpMethod;
//
//@Configuration
//@EnableWebSecurity
//@EnableMethodSecurity
//public class SecurityConfig {
//	@Bean
//	PasswordEncoder passwordEncoder() {
//		return new BCryptPasswordEncoder();
//	}
//
//
//    @Autowired
//    public void configure(AuthenticationManagerBuilder auth) throws Exception {
//        auth
//          .inMemoryAuthentication()
//          .withUser("user1")
//          .password(passwordEncoder().encode("user1Pass"))
//          .authorities("ROLE_USER");
//    }
//
//	@Bean
//	SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
//		http.csrf().disable().authorizeRequests()
//				.antMatchers("/", "/login","/register", "/detail").permitAll()
//				.antMatchers("/css/**", "/js/**", "/img/**", "**/favicon.ico").permitAll()
//				.antMatchers("/login/**").anonymous().anyRequest().authenticated()
//				.anyRequest().authenticated();
//
//		return http.build();
//	}
//	@Bean
//	WebSecurityCustomizer webSecurityCustomizer() {
//		return (web) -> web.ignoring().antMatchers("/css/**", "/js/**", "/img/**");
//	}

//	@Autowired
//    public void configureGlobal(AuthenticationManagerBuilder auth) throws Exception {
//        auth
//          .inMemoryAuthentication()
//          .withUser("user1")
//          .password(passwordEncoder().encode("user1Pass"))
//          .authorities("USER");
//    }

//	@Bean
//	UserDetailsService userDetailsService(PasswordEncoder encoder) {
//		UserDetails admin = User.withUsername("hach").password(encoder.encode("hacheery")).roles("ADMIN").build();
//		UserDetails user = User.withUsername("user").password(encoder.encode("pwd1")).roles("USER").build();
//		return new InMemoryUserDetailsManager(admin, user);
//	}
//
//	@Bean
//	SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
//		return http
//				.authorizeHttpRequests().antMatchers("/hello").permitAll()
//				.and()
//				.authorizeHttpRequests().antMatchers("/cart").authenticated()
//				.and().formLogin()
//				.and().build();
//	}
//
//	@Bean
//	public PasswordEncoder passwordEncoder() {
//		return new BCryptPasswordEncoder();
//	}
//
//}

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.AuthenticationProvider;
import org.springframework.security.authentication.ProviderManager;
import org.springframework.security.config.Customizer;
import org.springframework.security.config.annotation.method.configuration.EnableMethodSecurity;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.core.userdetails.User;
import org.springframework.security.authentication.dao.DaoAuthenticationProvider;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.security.provisioning.InMemoryUserDetailsManager;
import org.springframework.security.web.SecurityFilterChain;
//import org.springframework.security.core.userdetails.UserDetailsService;

@EnableWebSecurity
@Configuration
//@EnableMethodSecurity
public class SecurityConfig {
	@Bean
	public UserDetailsService userDetailsService(PasswordEncoder encoder) {
		UserDetails admin = User.withUsername("admin").password(encoder.encode("admin")).roles("ADMIN").build();
		UserDetails user = User.withUsername("user").password(encoder.encode("user")).roles("USER").build();
		return new InMemoryUserDetailsManager(admin, user);
	}

	@Bean
	public PasswordEncoder passwordEncoder() {
		return new BCryptPasswordEncoder();
	}

	@Bean
	public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
		return http.csrf().disable()
				.authorizeHttpRequests()
				.requestMatchers("/","/register", "/css/**", "/js/**", "/img/**").permitAll()
				.anyRequest().authenticated()
				.and()
				.formLogin().loginPage("/login").permitAll()
				.defaultSuccessUrl("/") // Redirect to /dashboard after login success
				.failureUrl("/login?success=false")
				.loginProcessingUrl("/j_spring_security_check")
				.and()
				.logout()
				.logoutSuccessUrl("/login")
				.and()
				.rememberMe()
				.userDetailsService(userDetailsService(passwordEncoder())) // Use the UserDetailsService bean to configure remember-me authentication
				.and()
				.build();
	}

	@Bean
	public AuthenticationProvider authenticationProvider() {
		DaoAuthenticationProvider provider = new DaoAuthenticationProvider();
		provider.setUserDetailsService(userDetailsService(passwordEncoder()));
		provider.setPasswordEncoder(passwordEncoder());
		return provider;
	}

	@Bean
	public AuthenticationManager authenticationManager() throws Exception {
		return new ProviderManager(List.of(authenticationProvider()));
	}


}
