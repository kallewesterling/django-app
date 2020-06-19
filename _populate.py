from dhri.parser import parse, test_integrity
from dhri.markdown_parser import get_raw_content, split_md_into_sections_batch
from dhri.meta import dhri_input, get_argparser, verify_url, load_data, save_data, delete_data, get_or_default, reset_all
from dhri.constants import BACKEND_AUTO, BRANCH_AUTO, AUTO_RESET, DELETE_FILE

if __name__ == '__main__':
  # Process arguments
  parser = get_argparser()
  args = parser.parse_args()

  # First check for reset
  if args.reset or AUTO_RESET == True:
    reset_all()

  if args.download:
    url = verify_url(args.download)
    
    branch = get_or_default('Branch', BRANCH_AUTO)

    data = get_raw_content(url, branch=branch)

    user = get_or_default('Username', data['meta']['user'])
    repo = get_or_default('Repository', data['meta']['repo_name'])
    name = get_or_default('Workshop name', repo.replace('-', ' ').title())
    
    data = split_md_into_sections_batch({'frontmatter', 'theory-to-practice', 'assessment'}, data['content'])
    
    data['meta'] = {
      'name': name,
      'parent_repo': f'{user}/{repo}',
      'parent_backend': BACKEND_AUTO,
      'parent_branch': branch
    }

    path = f'{repo}.json'
    if args.dest: path = args.dest

    save_data(path, data)

    _continue = dhri_input('Do you want to continue with this file? (Y/n) ', bold=True, color='yellow')
    if _continue == '' or _continue.lower() == 'y':
      pass # we continue
    else:
      exit()

  elif args.file:
    path = args.file

  else:
    args.error('Cannot interpret the arguments passed to the script. You need to provide either -f or -d. Try running it with argument -h to see more information.')

  # Now we load up the backend (we do it here because we don't want to load the whole django framework before, because it takes a second)
  from dhri.backend import workshop_magic, create_new_workshop, update_workshop
  from dhri.backend import Workshop, Frontmatter, Project, Resource, Reading, Contributor

  data = load_data(path)

  # Parse data
  data['frontmatter'] = parse(data['frontmatter'], 'frontmatter')
  data['theory-to-practice'] = parse(data['theory-to-practice'], 'theory-to-practice')
  data['assessment'] = parse(data['assessment'], 'assessment')

  # Test integrity for the data
  test_integrity(data)

  w = workshop_magic(data)


  if DELETE_FILE and path:
    delete_data(path, auto=True)

"""
  if existing == 0 or existing == 2:
    w = create_new_workshop(frontmatter)
  elif existing == 1:
    w = update_workshop(frontmatter)
"""