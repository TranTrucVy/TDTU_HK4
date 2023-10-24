package com.SpringCommerce.config.db;

import javax.sql.DataSource;

import org.apache.ibatis.session.SqlSessionFactory;
import org.mybatis.spring.SqlSessionFactoryBean;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.core.io.support.PathMatchingResourcePatternResolver;
import org.springframework.jdbc.datasource.DataSourceTransactionManager;

import com.SpringCommerce.config.AES;
import com.zaxxer.hikari.HikariConfig;
import com.zaxxer.hikari.HikariDataSource;

//@Configuration
public class DatabaseConfig {

//	@Value("${springcommerce.datasource.url}")
//	private String urlDB;
//
//	@Value("${springcommerce.datasource.username}")
//	private String userName;
//
//	@Value("${springcommerce.datasource.password}")
//	private String password;
//
//	@Value("${springcommerce.datasource.driver-class-name}")
//	private String driverClassName;
//	
//	private String secretKey = "Killa@1510";
//	
//	@Bean(name = "dataSource")
//	DataSource dataSource() {
//		HikariConfig hikariConfig = new HikariConfig();
//		hikariConfig.setJdbcUrl(AES.decrypt(urlDB, secretKey));
//		hikariConfig.setDriverClassName(this.driverClassName);
//		hikariConfig.setUsername(AES.decrypt(this.userName, secretKey));
//		hikariConfig.setPassword(AES.decrypt(this.password, secretKey));
//		HikariDataSource hikariDataSource = new HikariDataSource(hikariConfig);
//		return hikariDataSource;
//	}
//
//	@Bean(name = "transactionManager")
//	DataSourceTransactionManager dataSourceTransactionManager() {
//		return new DataSourceTransactionManager(dataSource());
//	}
//
//	@Bean(name = "sqlSessionFactory")
//	SqlSessionFactory sqlSessionFactory(@Qualifier("dataSource") DataSource dataSource) throws Exception {
//		SqlSessionFactoryBean sqlSessionFactoryBean = new SqlSessionFactoryBean();
//		sqlSessionFactoryBean.setDataSource(dataSource);
//		sqlSessionFactoryBean.setMapperLocations(new PathMatchingResourcePatternResolver()
//                .getResources("classpath:com/SpringCommerce/mapper/sql/*.xml"));
//		return sqlSessionFactoryBean.getObject();
//	}
}
