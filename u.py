
etiquetas=["work_year", "experience_level" ,"employment_type", "job_title","salary", "salary currency" , "salary_in_usd", "employee_residence", "remote_ratio", "company_location" , "company_size"]
print (etiquetas)

print ( etiquetas[2])



corr=salaries.set.index ("experience_level") 
sm.graphics.plot_corr(corr , xnames=etiquetas(corr.colums))
plt.show()