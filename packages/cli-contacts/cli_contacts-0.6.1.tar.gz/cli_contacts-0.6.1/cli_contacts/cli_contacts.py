from pathlib import Path
import click
from .models import Contacts, session, Base, engine
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import pandas as pd

Base.metadata.create_all(engine)

@click.group()
@click.version_option(version='0.6.1', prog_name='black-book')
def cli_contacts():
    pass

@cli_contacts.command()
@click.option('--name', help='Navn', prompt='Navn')
@click.option('--tlf', help='Telefonnummer', prompt='Telefonnr')
@click.option('--email', help='Email', prompt='Email')
@click.option('--arbejdsplads', help='Arbejdsplads', prompt='Arbejdsplads')
def create(name, tlf, email, arbejdsplads):
    '''
    Gemmer en ny kontakt i databasen.
    '''
    new_entry = Contacts(name=name, tlf=tlf, email=email, arbejdsplads=arbejdsplads)
    session.add(new_entry)
    session.commit()
    click.echo(f'{new_entry.name} gemt!')
    
@cli_contacts.command()
@click.argument('id')
@click.confirmation_option(prompt='Er du sikker på, at du vil slette denne kontakt?')
def delete(id):
    '''
    Sletter en række med et givent id!

    Id kan findes i search med --show-id.
    '''
    try:
        row = session.query(Contacts).filter(Contacts.id == int(id))
        click.echo(f'{row.first().name} slettet!')
        row.delete()
        session.commit()
    except:
        click.echo('Ingen række med det ID!')
        raise click.Abort()

@cli_contacts.command()
@click.argument('id')
@click.option('--name', default='', help='Nyt navn', prompt='Navn')
@click.option('--tlf', default='', help='Nyt telefonnummer', prompt='Telefonnr')
@click.option('--email', default='', help='Ny email', prompt='Email')
@click.option('--arbejdsplads', default='', help='Ny arbejdsplads', prompt='Arbejdsplads')
def update(id, name, tlf, email, arbejdsplads):
    '''
    Opdaterer en række med de givne informationer.

    ID kan findes i search.
    '''
    q = session.query(Contacts).get(int(id))
    
    q.name = q.name if name == '' else name
    q.tlf = q.tlf if tlf == '' else tlf
    q.email = q.email if email == '' else email
    q.arbejdsplads = q.arbejdsplads if arbejdsplads == '' else arbejdsplads

    session.commit()
    click.echo(f'{name} opdateret!')


@cli_contacts.command()
@click.argument('search_string', required=False)
@click.option('--id/--no-id', default=False, help='Vis ID eller ej')
@click.option('--name', '--n', 'parameter', flag_value="name", help="Søg efter navn")
@click.option('--tlf', '--t', 'parameter', flag_value="tlf", help="Søg efter telefonnr")
@click.option('--sted', '--s', 'parameter', flag_value="sted", help="Søg efter arbejdsplads")
@click.option('--alle', '--a', 'parameter', flag_value="alle", help="Vis alle kontakter i databasen")
def search(search_string, parameter, id):
    '''
    Søg efter kontakt i databasen.
    '''

    def print_resultat(query_object):
        if query_object.count() > 0:
            for person in query_object:
                if id == True:
                    fid = click.style(str(person.id), fg='green', bold=True)
                    click.echo(f'ID: {fid}')
                click.echo(f'Navn: {person.name}')
                click.echo(f'Tlf: {person.tlf}')
                click.echo(f'Email: {person.email}')
                click.echo(f'Arbjedssted: {person.arbejdsplads}')
                if query_object.count() > 1:
                    afslut = click.style('----------', bold=True)
                    click.echo(afslut)

    if parameter == 'alle':
        print_resultat(session.query(Contacts))

    if parameter == 'name':
        if search_string is None:
            click.echo('Du mangler at definere [SEARCH_STRING]')
        else:
            query = session.query(Contacts).filter(Contacts.name.like(f'%{search_string}%'))
            print_resultat(query)
    elif parameter == 'tlf':
        if search_string is None:
            click.echo('Du mangler at definere [SEARCH_STRING]')
        else:
            query = session.query(Contacts).filter(Contacts.tlf.like(f'%{search_string}%'))
            print_resultat(query)
    elif parameter == 'sted':
        if search_string is None:
            click.echo('Du mangler at definere [SEARCH_STRING]')
        else:
            query = session.query(Contacts).filter(Contacts.arbejdsplads.like(f'%{search_string}%'))
            print_resultat(query)
    else:
        query = session.query(Contacts).filter(Contacts.name.like(f'%{search_string}%'))
        print_resultat(query)

@cli_contacts.command()
@click.option('--format', type=click.Choice(['CSV', 'DRIVE'], case_sensitive=False), default='CSV', show_default=True, help='Det format, der skal tages backup til')
@click.option('--filepath', type=click.Path(), help="Sti til csv fil. Skal defineres med filnavn")
def backup_db(format, filepath):
    '''
    Tager backup af databasen til en Google Drive konto eller en csv fil!

    Hvis man tager backup til csv, så skal man definere en --filepath
    '''
    if format == 'DRIVE':
        gauth = GoogleAuth()
        gauth.LocalWebserverAuth()
        drive = GoogleDrive(gauth)

        db_path = Path.home() / '.contacts.db'

        db_file = drive.CreateFile({'mimetype': 'application/x-sqlite3'})
        db_file['title'] = db_path.name
        db_file.SetContentFile(db_path.__str__())
        db_file.Upload()
        click.echo('Dine kontakter er uploaded til din Google Drive!')
    else:
        if not filepath:
            raise click.ClickException('Du skal definere filepath med --filepath!')
        else:
            alle_kontakter = list(Contacts.select().dicts())
            df = pd.DataFrame(alle_kontakter)
            df.to_csv(filepath, index=False)
            click.echo(f'Dine kontakter er exporteret til {filepath}')
