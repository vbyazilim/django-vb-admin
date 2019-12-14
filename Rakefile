task :default => [:install]

desc "Remove/Delete build..."
task :clean do
  rm_rf %w(build dist)
  rm_rf Dir.glob("*.egg-info")
  puts "Build files are removed..."
end

desc "Install package for local development purpose"
task :install => [:build] do
  system "pip install -e ."
end

desc "Build package"
task :build => [:clean] do
  system "python setup.py sdist bdist_wheel"
end

namespace :upload do
  desc "Upload package to main distro (release)"
  task :main => [:build] do
    puts "Uploading package to MAIN distro..."
    system "twine upload --repository pypi dist/*"
  end
  desc "Upload package to test distro"
  task :test => [:build] do
    puts "Uploading package to TEST distro..."
    system "twine upload --repository testpypi dist/*"
  end
end

AVAILABLE_REVISIONS = ["major", "minor", "patch"]
desc "Bump version: #{AVAILABLE_REVISIONS.join(',')}"
task :bump, [:revision] do |t, args|
  args.with_defaults(revision: "patch")
  abort "Please provide valid revision: #{AVAILABLE_REVISIONS.join(',')}" unless AVAILABLE_REVISIONS.include?(args.revision)
  system "bumpversion #{args.revision}"
end

namespace :docs do
  desc "Run docs server"
  task :serve do
    system "mkdocs serve -a 0.0.0.0:8000"
  end
  
  desc "Build docs"
  task :build do
    system "mkdocs build --clean"
  end

  desc "Deploy to github"
  task :deploy do
    system "mkdocs gh-deploy"
  end
end
