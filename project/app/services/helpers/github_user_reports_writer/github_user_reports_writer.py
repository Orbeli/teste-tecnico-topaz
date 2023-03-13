import os.path as path

from app.domain.usecases import GetGithubUserReportsResponse

def generate_report_file(self, file_name: str, report_data: GetGithubUserReportsResponse):
    file_path =  path.abspath(path.join(__file__ ,"../../../../github_reports_file"))
    file_name = f"{file_path}/{file_name}.txt"
    with open(file_name, 'w') as report_file:
        report_file.write(f'Nome: {report_data.name}\n')
        report_file.write(f'Perfil: {report_data.profile}\n')
        report_file.write(f'Número de repositórios públicos: {len(report_data.repositories)}\n')
        report_file.write(f'Número de seguidores: {report_data.followers}\n')
        report_file.write(f'Número de usuários seguidos: {report_data.following}\n')
        report_file.write(f'repositórios:\n')
        for repo_name, repo_url in report_data.repositories.items():
            report_file.write(f'\t {repo_name}: {repo_url}\n')
