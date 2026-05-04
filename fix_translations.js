const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');
const regex = /const translations = (\{.*?\});/s;
const match = html.match(regex);
if (match) {
    let translations = JSON.parse(match[1]);
    delete translations.exp1_role;
    delete translations.exp1_meta;
    delete translations.exp1_desc_1;
    delete translations.exp1_desc_2;
    delete translations.exp1_desc_3;
    delete translations.exp1_desc_4;
    delete translations.exp1_desc_5;
    
    translations.exp2_desc_1 = { es: 'Monitoreo y Mantenimiento de Pipelines: Supervisión diaria de los procesos de carga (ETL) para asegurar que los datos estén disponibles y actualizados para las áreas de negocio al inicio de la jornada.', en: 'Pipeline Monitoring and Maintenance: Daily supervision of load processes (ETL) to ensure data is available and updated for business areas at the start of the day.' };
    translations.exp2_desc_2 = { es: 'Validación de Calidad (Data Quality): Ejecución de scripts de control para detectar anomalías, duplicados o valores nulos en las bases de datos transaccionales del banco.', en: "Quality Validation (Data Quality): Execution of control scripts to detect anomalies, duplicates, or null values in the bank's transactional databases." };
    translations.exp2_desc_3 = { es: 'Extracción Bajo Demanda: Atención a requerimientos ad-hoc de diversas áreas (Riesgos, Finanzas, Comercial), traduciendo necesidades de negocio en consultas SQL complejas y eficientes.', en: 'On-Demand Extraction: Handling ad-hoc requirements from various areas (Risk, Finance, Commercial), translating business needs into complex and efficient SQL queries.' };
    translations.exp2_desc_4 = { es: 'Gestión de Dashboards: Actualización y ajuste de tableros en Power BI / Tableau, asegurando que los KPIs reflejen la realidad operativa actual.', en: 'Dashboard Management: Updating and adjusting dashboards in Power BI/Tableau, ensuring KPIs reflect the current operational reality.' };
    translations.exp2_desc_5 = { es: 'Documentación Técnica: Registro diario de cambios en los diccionarios de datos y mantenimiento de la trazabilidad (lineage) de la información.', en: 'Technical Documentation: Daily log of changes in data dictionaries and maintenance of information traceability (lineage).' };
    
    translations.nav_education = { es: 'Educación', en: 'Education' };
    translations.section_education = { es: 'Educación', en: 'Education' };
    translations.edu1_title = { es: 'Bachelors Computer Science', en: 'Bachelors Computer Science' };
    translations.edu1_school = { es: 'EIDHI INTERNATIONAL UNIVERSITY - BOSTON', en: 'EIDHI INTERNATIONAL UNIVERSITY - BOSTON' };
    translations.edu1_meta = { es: 'Boston, United States', en: 'Boston, United States' };
    
    html = html.replace(regex, 'const translations = ' + JSON.stringify(translations) + ';');
    fs.writeFileSync('index.html', html);
    console.log('Translations updated!');
}
